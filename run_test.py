import pytest

pytest.main([
    "-v",
    "--html=reports/report.html",
    "--self-contained-html"
])
