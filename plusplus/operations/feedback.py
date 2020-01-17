import json

def generate_feedback_form():
    # construct modal form
    modal = {
    	"type": "modal",
    	"title": {
    		"type": "plain_text",
    		"text": "Feedback"
    	},
    	"submit": {
    		"type": "plain_text",
    		"text": "Submit"
    	},
    	"close": {
    		"type": "plain_text",
    		"text": "Cancel"
    	},
    	"blocks": [
    		{
                "block_id": "email",
    			"type": "input",
    			"element": {
    				"type": "plain_text_input",
    				"placeholder": {
    					"type": "plain_text",
    					"text": "Enter a valid email"
    				}
    			},
    			"label": {
    				"type": "plain_text",
    				"text": "Contact Email",
    			}
    		},
    		{
                "block_id": "feedback",
    			"type": "input",
    			"element": {
    				"type": "plain_text_input",
    				"multiline": True,
    				"placeholder": {
    					"type": "plain_text",
    					"text": "Your feedback here"
    				}
    			},
    			"label": {
    				"type": "plain_text",
    				"text": "Feedback"
    			}
    		}
    	]
    }
    return json.dumps(modal)
