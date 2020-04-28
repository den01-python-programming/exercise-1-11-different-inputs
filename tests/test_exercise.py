import pytest
import src.exercise

def test_exercise():
    input_values = ["bye","114","4.6","False"]
    input_values_stored = ["bye","114","4.6","False"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2],output[3]] == ["Give a string:","Give an integer:","Give a float:","Give a boolean:"]
    assert [output[4],output[5],output[6],output[7]] == ["You gave the string " + input_values_stored[0],\
                                                         "You gave the integer " + input_values_stored[1],\
                                                         "You gave the float " + input_values_stored[2],\
                                                         "You gave the boolean " + input_values_stored[3]]
