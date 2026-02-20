import pytest
from vantix.main import parse_packages, build_install_list

def test_parse_packages_simple():
    args = ["--pkg", "numpy"]
    packages = parse_packages(args)
    assert "numpy" in packages
    assert packages["numpy"] is None

def test_parse_packages_version():
    args = ["--pkg", "numpy==1.24.0"]
    packages = parse_packages(args)
    assert packages["numpy"] == "1.24.0"

def test_parse_packages_latest():
    args = ["--pkg", "numpy==latest"]
    packages = parse_packages(args)
    assert packages["numpy"] is None

def test_parse_packages_multiple():
    args = ["--pkg", "numpy", "--pkg", "pandas==2.0.0"]
    packages = parse_packages(args)
    assert packages["numpy"] is None
    assert packages["pandas"] == "2.0.0"

def test_build_install_list():
    packages = {"numpy": None, "pandas": "2.0.0"}
    install_list = build_install_list(packages)
    assert "numpy" in install_list
    assert "pandas==2.0.0" in install_list
