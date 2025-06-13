@echo off
pytest -v -s -m Purchase --alluredir=Python_BDD_Framwork\reports\allure-results
allure generate Python_BDD_Framwork\reports\allure-results -o Python_BDD_Framwork\reports\allure-report --clean
@REM allure open Python_BDD_Framwork\reports\allure-report
