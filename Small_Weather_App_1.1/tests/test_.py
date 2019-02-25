
import main

def test_empty_db(main):
    rv = main.get('/login')
    assert b'No entries here so far' in rv.data
  
