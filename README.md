Представляю проект по автоматизации тестирования UI раздела Elements сайта DEMOQA.
Основными технологиями, которыми я пользовался входе реализации представленного проекта, являются Selenium,Pytest, Allure-Report,Requests и другие библиотеки, указанные в файле requirements.txt
При написании автотестов использовал паттер PageObject.
Далее я дам описание директорий проекта.
LOCATORS- директория, содержащая в себе основные локаторы веб-элементов, с которыми я взаимодействовал при написании автотестов.Также содержит основные методы для работы с элементами на веб-страницах.
PAGES - директория, содержащая в себе базовые методы для работы с webdriver.
TESTS- директория, которая реализует тесты.
allure-report- cодержит актуальный allure отчет о проведении тестов.
data- директория, содержащая в себе классы, описывающие пользователя.
generator- директория, содержащая в себе основные методы генерации данных пользователя.
сonfest- файл, позволяющий реализовывать Pytest-фикстуру.
requirements.txt- файл, содержащий в себе библиотеки, используемые при работе над проектом.
