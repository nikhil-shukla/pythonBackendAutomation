# Created by shukla at 11-01-2022
Feature: Verify if books are added and deleted using library API
  # Enter feature description here

  @smoke @library
  Scenario: Verify AddBook API functionality
    Given the book details which needed to be added to library
    When we execute the AddBook API method
    Then book is successfully added
    And status code of response should be 200

  @regression @library
  Scenario Outline: Verify AddBook API functionality using Data parameterization
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook API method
    Then book is successfully added
      Examples:
        |isbn     |aisle |
        |fdjasjfal|433   |
        |fdjasdsjfal|545   |