from unittest.mock import patch

from hamcrest import (
    assert_that,
    contains,
    equal_to,
    has_entries,
    is_,
)
from microcosm_postgres.context import SessionContext, transaction
from microcosm_postgres.identifiers import new_object_id
from microcosm_postgres.operations import recreate_all

from rob_onboarding.app import create_app
from rob_onboarding.models.order_model import Order


class TestOrderRoutes:
    list_create_uri = "/api/v1/order"

    def setup(self):
        self.graph = create_app(testing=True)
        self.client = self.graph.flask.test_client()
        recreate_all(self.graph)

        self.order_id = new_object_id()
        self.order1 = Order(
            id=self.order_id, customer_id=new_object_id()
        )
        self.detail_uri = f"/api/v1/order/{self.order1.id}"

    def teardown(self):
        self.graph.postgres.dispose()

    def test_search(self):
        with SessionContext(self.graph), transaction():
            self.order1.create()

        response = self.client.get(self.list_create_uri)
        assert_that(response.status_code, is_(equal_to(200)))
        assert_that(
            response.json,
            has_entries(
                items=contains(
                    has_entries(
                        id=str(self.order1.id),
                        customerId=str(self.order1.customer_id)
                    )
                )
            )
        )

    def test_create(self):
        customer_id = str(new_object_id())
        with patch.object(self.graph.order_store, "new_object_id") as mocked:
            mocked.return_value = self.order1.id
            response = self.client.post(
                self.list_create_uri, json=dict(customerId=customer_id)
            )
        assert_that(response.status_code, is_(equal_to(201)))
        assert_that(
            response.json,
            has_entries(
                id=str(self.order1.id),
                customerId=str(customer_id)
            )
        )

    def test_retrieve(self):
        with SessionContext(self.graph), transaction():
            self.order1.create()

        uri = f"/api/v1/order/{self.order1.id}"

        response = self.client.get(uri)

        assert_that(
            response.json,
            has_entries(
                id=str(self.order1.id),
                customerId=str(self.order1.customer_id),
            ),
        )

    def test_delete(self):
        with SessionContext(self.graph), transaction():
            self.order1.create()

        response = self.client.delete(self.detail_uri)
        assert_that(response.status_code, is_(equal_to(204)))

        with SessionContext(self.graph) as session:
            assert session.session.query(Order).get(self.order_id) is None
