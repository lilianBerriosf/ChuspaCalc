import sys
from unittest.mock import MagicMock, patch
from escuadra.core import dispatcher

def test_dispatch_subcomando_desconocido(capsys):
    with patch("escuadra.core.registry.buscar_por_nombre", return_value=None):
        codigo = dispatcher.dispatch("no_existe")
    assert codigo == 1
    captured = capsys.readouterr()
    assert "subcomando desconocido" in captured.err

def test_dispatch_subcomando_conocido():
    mock_cls = MagicMock()
    mock_instance = MagicMock()
    mock_cls.return_value = mock_instance
    with patch("escuadra.core.registry.buscar_por_nombre", return_value=mock_cls):
        codigo = dispatcher.dispatch("karnaugh")
    assert codigo == 0
    mock_cls.assert_called_once()

def test_dispatch_error_importacion(capsys):
    mock_cls = MagicMock(side_effect=ImportError("no disponible"))
    with patch("escuadra.core.registry.buscar_por_nombre", return_value=mock_cls):
        codigo = dispatcher.dispatch("falla")
    assert codigo == 1