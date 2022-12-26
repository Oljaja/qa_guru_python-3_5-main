import os.path

from selene import have, command
from selene.support.shared import browser


def test_complete_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    # WHEN

    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('Fa')
    browser.element('#userEmail').type('opuss77@gmail.com')

    browser.all('[for^=gender-radio-2]').element_by(have.text('Female')).click()
    browser.element('#userNumber').type('8977777151')

    # browser.element('#dateOfBirthInput').perform(command.js.set_value('12-12-2000'))

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('December')
    browser.element('.react-datepicker__year-select').type(2000)
    browser.element('.react-datepicker__day--012:not(.react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').type('commerce').press_enter()
    browser.element('[for ="hobbies-checkbox-1"]').click()
    browser.element('[for ="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'foto/111.jpg')))

    browser.element('#currentAddress').type('Minskay')

    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()



    # THEN

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Olga Fa',
        'opuss77@gmail.com',
        'Female',
        '8977777151',
        '12 December,2000',
        'Commerce',
        'Sports, Reading',
        '111.jpg',
        'Minskay',
        'Uttar Pradesh Agra'
    )
    )
