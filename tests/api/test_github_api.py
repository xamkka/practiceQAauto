import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('sergii_butenko') 
    assert r['message'] == 'Not Found'

    
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('practiceQAauto')
    ##print(r)
    assert r['total_count'] == 2
    assert 'practiceQAauto' in r['items'][1]['name']

@pytest.mark.api
def test_repo_not_found(github_api):
    r = github_api.search_repo('practiceQAauto_repo_not_found')
    assert r['total_count'] == 0
    


@pytest.mark.api
def test_repo_with_single_char_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
   

@pytest.mark.api
def test_emoji_present(github_api):
    r = github_api.get_emoji()
    assert 'ambulance' in r


@pytest.mark.api
def test_emoji_not_present(github_api):
    r = github_api.get_emoji()
    assert 'ambulance1' not in r


@pytest.mark.api
def test_commits(github_api):
    r = github_api.get_commits('defunkt', 'github-gem')
    print(r)