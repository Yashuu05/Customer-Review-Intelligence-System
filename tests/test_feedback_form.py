import pytest
from APP.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_feedback_form_live_toggle(client):
    # Initially should be False
    from APP.main import feedback_is_live
    
    # Try to access feedback when closed
    response = client.get('/feedback')
    assert b'Form Closed' in response.data or b'currently not accepting' in response.data

    # Launch it
    client.post('/admin/launch_feedback')
    response = client.get('/feedback')
    assert b'Product' in response.data  # Ensure our new product field is there
    
    # Close it
    client.post('/admin/close_feedback')
    response = client.get('/feedback')
    assert b'Form Closed' in response.data or b'currently not accepting' in response.data
