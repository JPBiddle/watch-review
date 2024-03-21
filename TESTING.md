# Joel's Watch Club Matching Testing

[Main README.md file](https://github.com/JPBiddle/watch-review/blob/main/README.md)

[View Live Project]()

# Contents

- [Joel's Watch Club Testing](#joels-watch-club-testing)
- [Contents](#contents)
  - [Testing User Stories](#testing-user-stories)
    - [First time visitor](#first-time-visitor)
    - [Returning visitor](#returning-visitor)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
    - [Code Validation](#code-validation)
    - [Lighthouse](#lighthouse)
  - [Further Testing](#further-testing)

---

## Testing User Stories

### First time visitor

- As a first time visitor, I would like to be able view content easily.

  - Reviews are displayed on the home page, available without login
  - Clicking on a review brings up a page with the full content.
  - The about page and social links are working at the bottom of all pages.

- First time visitors want to be able to create an account and start posting content.

  - The user is guided easily to the sign up page via sign in.

- As a first time visitor I want to know what the site is about.
  - The about page gives detail about what the purpose of the site is.

### Returning visitor

- As a returning visitor, I would like to access my content seperately from the main content.

  - After logging in all the users content is visible to them on the dashboard.

- As a returning visitor I would to edit or delete my previous content as well as post new content.
  - Edit and delete functions are available on the dashboard, and access to post reviews is granted.

---

## Manual Testing

Extensive testing was conducted manually to ensure all parts of the website function as intended.
Below are screenshots of the testing in progress, going through each page and checking everything functions.

### Home

Testing that reviews appear on home page, are clickable and appear latest at the top by date.

<details>

<summary>Reviews on home</summary>

![Home](reviews/static/assets/img/testing_img/test(16).png)

</details>

<details>

<summary>Review on click, checking for content</summary>

![Home](reviews/static/assets/img/testing_img/test(18).png)

</details>

<details>

<summary>Review on click, checking for content, scrolled</summary>

![Home](reviews/static/assets/img/testing_img/test(19).png)

</details>

<details>

<summary>About page</summary>

![Home](reviews/static/assets/img/testing_img/test(13).png)

</details>

### Navigation

Testing that 'Add Review' login required

<details>

<summary>Login Required</summary>

![login Required](reviews/static/assets/img/testing_img/test(14).png)

</details>


Testing that 'My Reviews' login required


<details>

<summary>Login Required</summary>

![login Required](reviews/static/assets/img/testing_img/test(15).png)

</details>

### Sign up

Testing the sign up page to ensure reuired fields, password confirmed, ensure user doesn't already exist and if so, please choose a different username.

<details>

<summary>Username required for sign up</summary>

![Sign up](reviews/static/assets/img/testing_img/test(1).png)

</details>

<details>

<summary>Password required for sign up</summary>

![Sign up](reviews/static/assets/img/testing_img/test(2).png)

</details>

<details>

<summary>Passwords don't match</summary>

![Sign up](reviews/static/assets/img/testing_img/test(24).png)

</details>

<details>

<summary>Passwords match</summary>

![Sign up](reviews/static/assets/img/testing_img/test(25).png)

</details>

<details>

<summary>Username exists</summary>

![Sign up](reviews/static/assets/img/testing_img/test(26).png)

</details>

<details>

<summary>Successfully created user, redirect to sign in</summary>

![Sign up](reviews/static/assets/img/testing_img/test(27).png)

</details>



### Sign in

Testing sign in page, checking form requirements, entering a user that doesn't exist and entering password incorrectly.

<details>

<summary>Sign in from nav</summary>

![Sign in](reviews/static/assets/img/testing_img/test(20).png)

</details>

<details>

<summary>User doesnt exist</summary>

![Sign in](reviews/static/assets/img/testing_img/test(21).png)

</details>

<details>

<summary>Check required form</summary>

![Check Req 1](reviews/static/assets/img/testing_img/test(22).png)

</details>

<details>

<summary>Check required form</summary>

![Check Req 2](reviews/static/assets/img/testing_img/test(23).png)

</details>

<details>

<summary>Check incorrect password</summary>

![Sign in](reviews/static/assets/img/testing_img/test(29).png)

</details>

<details>

<summary>Successful sign in</summary>

![Sign in](reviews/static/assets/img/testing_img/test(17).png)

</details>

### Log out

After successful login, log out and return to sign in page.

<details>

<summary>Successful log out</summary>

![log out](reviews/static/assets/img/testing_img/test(12).png)

</details>


### Add Review page

Add review page has been tested ensure it cannot be accessed before login - now a test login is used to fill out the add review page and submit it, checking the review appears on home page and in user dashboard.

<details>

<summary>Page accessed with login</summary>

![Add review](reviews/static/assets/img/testing_img/test(4).png)

</details>

<details>

<summary>Check required fields</summary>

![Add review](reviews/static/assets/img/testing_img/test(5).png)

</details>

<details>

<summary>Test review posted with flash message, appears in dashboard</summary>

![Add review](reviews/static/assets/img/testing_img/test(6).png)

</details>

<details>

<summary>Review appears on home page</summary>

![Add review](reviews/static/assets/img/testing_img/test(7).png)

</details>

<details>

<summary>Review when clicked</summary>

![Add review](reviews/static/assets/img/testing_img/test(30).png)

</details>

### Edit review

On the dashboard the user may edit a review. The dashboard has been tested to check that it doesn't allow users to access it without login. The edit page was tested to check required fields and then the test review was edited - the edit was reflected on the dashboard and home page.

<details>

<summary>Edit page form populated with existing test post</summary>

![Edit review](reviews/static/assets/img/testing_img/test(31).png)

</details>

<details>

<summary>Edited post with changes in dashboard, plus flash message</summary>

![Edit review](reviews/static/assets/img/testing_img/test(9).png)

</details>

### Delete post

On the user dashboard, the delete post function was tested. The correct modal popped up to warn users that deletion was permanent, and when confirmed the post disappeared from home page and dashboard, with flash message appearing.

<details>

<summary>Delete message modal</summary>

![Edit review](reviews/static/assets/img/testing_img/test(10).png)

</details>

<details>

<summary>Delete confirmed</summary>

![Edit review](reviews/static/assets/img/testing_img/test(11).png)

</details>

---

## Automated Testing

### Lighthouse

Part of my testing was using Lighthouse from Chrome to check accessibility, SEO performance and general loading performance.
Below is a screenshot of the current Lighthouse results.

Upon testing with lighthouse I was satisfied with all pages other than home - the Clean Blog theme I used had an excess of CSS in the CSS file I imported, which was slowing loading somewhat.

If I had more time I would clean this up and in future I will be very careful about importing themes.

<details>

<summary>Lighthouse Home</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_1.png)

</details>

<details>

<summary>Lighthouse Sign in</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_2.png)

</details>

<details>

<summary>Lighthouse Dashboard</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_3.png)

</details>

<details>

<summary>Lighthouse review example</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_4.png)

</details>

<details>

<summary>Lighthouse Edit</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_5.png)

</details>

<details>

<summary>Lighthouse add review</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_6.png)

</details>

<details>

<summary>Lighthouse sign up</summary>

![Lighthouse](reviews/static/assets/img/testing_img/lighthouse_7.png)

</details>


End of TESTING Doc
---