import pytest
import requests

from catinabox import catgenerator


# Write tests for the refactored `catinabox.catgenerator`


def test__cat_birthday(mocker):
    # How to mock 'birthday' when it is the result of a random
    # function that is itself the result of another mocked function, time?
    # If randint is mocked, it bypasses the calculation of birthday.
    # Solution: use assert_called_with on randint
    # set age at 4.5 years:
    mocker.patch('time.time', return_value=1523134769.2669976)
    mocker.patch('random.randint', return_value=1523134769 -
                 365*24*60*60*4.5)
    cat_bd = catgenerator.cat_birthday()
    # assert age == 365*24*60*60*4.5
    assert cat_bd == '2013-10-08 04:59:29'


# correct except for whatever requests exception, must be actual exception?
def test__name_cat_requests_error(mocker):
    # test unavailable server:
    #  mocker.patch('requests.get', side_effect=raiseerror)
    mocker.patch('requests.get', side_effect=requests.exceptions.Timeout)
    with pytest.raises(catgenerator.CouldNotGetNameError):
        catgenerator.name_cat()


def test__name_cat(mocker):
    # this goes in a separate test:
    # test name returned: 'Morris', needs to be json obj, not string:
    # instead of this:
    #  mocker.patch('requests.get', return_value=['Morris'])
    # need to specify return_value as a json object:
    mocker.patch('requests.get').return_value.json.return_value = ['Morris']
    assert catgenerator.name_cat() == 'Morris'


def test__cat_generator(mocker):
    # This is wrong; cannot patch in the style above for functions of modules.
    # Why not? Instead must use mocker.patch.object :
    #  mocker.patch('catgenerator.name_cat', return_value='Mittens')
    mocker.patch.object(catgenerator, 'name_cat', return_value='Mittens')
    mocker.patch.object(catgenerator, 'cat_birthday',
                        return_value='2013-12-02 07:57:09')
    assert next(catgenerator.cat_generator()) == {
        "name": 'Mittens', "birthday": '2013-12-02 07:57:09'}
