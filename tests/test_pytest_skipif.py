import pytest

system_version = "v1.2.0"

@pytest.mark.skipif(
    system_version == "v1.3.0", reason ="Тест не может быть запущен на версии системы 1.3.0"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    system_version == "v1.2.0", reason ="Тест не может быть запущен на версии системы 1.2.0"
)
def test_system_version_invalid():
    ...