from .hello_world import print_hello_world

def test_print_hello_world(capsys):
    # Call the function
    print_hello_world()
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output is "Hello, world!" followed by a newline
    assert captured.out == "Hello, world!\n"