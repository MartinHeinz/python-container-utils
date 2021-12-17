from .context import container_utils


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    container_utils.Blueprint.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out
