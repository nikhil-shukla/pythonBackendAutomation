# Created by shukla at 11-01-2022
Feature: Github API Validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credentials
    When I hit gitRepo API of github
    Then status code of response should be 200