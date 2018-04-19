from qamplus.base import QamPlusClient

import unittest


class TestModels(unittest.TestCase):
    execution_logic= {
        "initial": "answer",
		"steps":
		[
			{"name":"play", "data":"silence/1" },
            {"name": "conference", "data":""}
        ]
    }

    reference_logic = {
        "initial": "answer",
        "steps":
            [
                {"name": "play", "data": "silence/1"}
            ]
    }
    customer_id = ''
    password = ''

    update_logic = {
        "initial": "answer",
        "steps":
            [
                {"name": "play", "data": "1_en"},
                {"name": "play", "data": "2_en"},
            ]
    }

    phone_number = ''

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass

    def test_create_new_call_outbound(self):
        client = QamPlusClient(customer_id=self.customer_id, password=self.password)
        response = client.voice.create(direction="outbound",
            to=self.phone_number,
            caller_id="12123456781",
            execution_logic=self.execution_logic,
            reference_logic=self.reference_logic,
            country_iso2="us",
            technology="pstn",
            status_callback_uri='')

        assert response is not None
        assert response.status_code == 200

        status = client.voice.get_status(
            reference_id=response.json.get('reference_id'))

        assert status is not None
        assert status.status_code == 200


        update_response = client.voice.update(
            reference_id=response.json.get('reference_id'),
            execution_logic=self.update_logic
        )

        assert update_response is not None
        assert update_response.status_code == 200

        delete_response = client.voice.delete(
            reference_id=response.json.get('reference_id')

        )



        status = client.voice.get_status(
            reference_id=response.json.get('reference_id'))

        assert status is not None
        assert status.status_code == 200
    #
    # def test_get_status(self):
    #     client = QamPlusClient(customer_id=self.customer_id, password=self.password)
    #     response = client.voice.get_status(
    #        reference_id='')
    #
    #     assert response is not None
    #     assert response.status_code == 200
    #
    #
    # def test_modify_live_call(self):
    #     client = QamPlusClient(customer_id=self.customer_id, password=self.password)
    #     response = client.voice.get_status(
    #        reference_id='')
    #
    #     assert response is not None
    #     assert response.status_code == 200
    #
    #
    # def test_hangup_call(self):
    #     client = QamPlusClient(customer_id=self.customer_id, password=self.password)
    #     response = client.voice.get_status(
    #        reference_id='')
    #
    #     assert response is not None
    #     assert response.status_code == 200