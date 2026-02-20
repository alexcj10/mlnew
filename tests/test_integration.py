import os
import shutil
import pytest
from pathlib import Path
from mlnew.main import create_project

from unittest.mock import patch, MagicMock

def test_full_project_creation(tmp_path):
    # Change to temp directory for the test
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    project_name = "test_ml_project"
    packages = {"numpy": None, "pandas": "2.0.0"}
    
    try:
        # Mock subprocess.run to avoid the overhead of venv creation and git init
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="Mocked output", stderr="")
            
            create_project(project_name, packages)
            
            project_path = tmp_path / project_name
            assert project_path.exists()
            assert (project_path / "data/raw").exists()
            assert (project_path / "src/training/train.py").exists()
            assert (project_path / "README.md").exists()
            assert (project_path / "SETUP_GUIDE.md").exists()
            assert (project_path / "requirements.txt").exists()
            
            # Verify README content contains the project name
            readme_content = (project_path / "README.md").read_text()
            assert project_name in readme_content
            assert "numpy" in readme_content
            assert "pandas==2.0.0" in readme_content
            
    finally:
        os.chdir(original_cwd)

def test_project_folder_exists(tmp_path):
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    project_name = "exists_test"
    (tmp_path / project_name).mkdir()
    
    try:
        with pytest.raises(SystemExit):
            create_project(project_name, {})
    finally:
        os.chdir(original_cwd)
