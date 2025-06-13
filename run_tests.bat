@echo off
pytest -v -s -m Purchase --alluredir=Python_BDD_Framwork\reports\allure-results
@REM allure generate Python_BDD_Framwork\reports\allure-results -o Python_BDD_Framwork\reports\allure-report --clean
allure open Python_BDD_Framwork\reports\allure-report
