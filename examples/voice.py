from qamplus.base import QamPlusClient

execution_logic= {
        "initial": "answer",
		"steps":
		[
			{"name":"play", "data":"2_en" },
            {"name":"conference", "data":"" },
			{"name":"play", "data":"2_en" }
        ]
    }

customer_id = 'abcd...'
password = 'password'
phone_number = '19876543210'

client = QamPlusClient(customer_id, password)
response = client.voice.create(direction="outbound",
                               to=phone_number,
                               caller_id="12123456789",
                               execution_logic=execution_logic,
                               reference_logic=execution_logic,
                               country_iso2="us",
                               technology="pstn")
