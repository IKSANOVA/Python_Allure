rem pip install allure-pytest
del /q C:\Users\liksanova\Documents\python_allure_tests\reports\*
py.test --alluredir=C:\Users\liksanova\Documents\python_allure_tests\reports
call C:\Users\liksanova\Documents\python_allure_tests\allure-2.13.3\bin\allure.bat serve C:\Users\liksanova\Documents\python_allure_tests\reports -h localhost