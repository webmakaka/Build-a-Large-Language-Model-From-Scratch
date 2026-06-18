import subprocess


def test_gpt_class_finetune():
    command = ["python", "ch06/01_main-chapter-code/gpt_class_finetune.py", "--test_mode"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0, f"Script exited with errors: {result.stderr}"
