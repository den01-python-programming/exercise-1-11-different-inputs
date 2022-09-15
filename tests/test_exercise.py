import pytest
import src.exercise

def test_exercise():
    input_values = ["bye","114","4.6"]
    input_values_stored = ["bye","114","4.6"]
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

    assert [output[0],output[1],output[2]]] == ["Give a string:","Give an integer:","Give a float:"]
    assert [output[3],output[4],output[5]] == ["You gave the string " + input_values_stored[0],\
                                                         "You gave the integer " + input_values_stored[1],\
                                                         "You gave the float " + input_values_stored[2]]
