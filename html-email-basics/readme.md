# HTML Email Basics

Welcome to the HTML Email Basics guide. This document aims to help you understand the fundamentals of creating HTML emails and ensuring their compatibility across various email clients.

## Table of Contents

- [Introduction](#introduction)
- [Why HTML Emails Are Different](#why-html-emails-are-different)
- [HTML Email Structure](#html-email-structure)
- [Styling Emails](#styling-emails)
- [Images in Emails](#images-in-emails)
- [Testing and Troubleshooting](#testing-and-troubleshooting)
- [Best Practices](#best-practices)
- [Resources](#resources)

## Introduction

HTML emails have their own unique challenges and requirements compared to web development. This guide will help you navigate the intricacies of creating effective and cross-compatible HTML emails.

## Why HTML Emails Are Different

HTML emails present unique challenges compared to standard web pages for several reasons:

1. **Complex Table Structures**: In email development, you often rely on HTML tables (`<table>`, `<tr>`, `<td>`) for layout and structuring your content. This is different from modern web development, where CSS Flexbox and Grid Layout are more common.

2. **Inconsistent Rendering**: HTML emails can render differently across various web browsers and email clients. Email clients often have varying levels of support for HTML and CSS, requiring you to design with cross-compatibility in mind.

3. **Accessibility Considerations**: Creating accessible HTML emails is essential. You must take into consideration people with various disabilities, such as those who use screen readers. This involves providing alternative text for images, ensuring a logical reading order, and following accessibility best practices.

4. **Use of Markup Languages**: While HTML and inline CSS are prevalent in email development, you can also utilize specialized markup languages like MJML (Mailjet Markup Language) to simplify the email creation process and improve compatibility.


## HTML Email Structure

When creating HTML emails, it's essential to follow certain best practices to ensure that your emails are effective and well-received. Here are some key considerations for structuring your HTML emails:

1. **Subject Line and Pre-header**: Craft an engaging subject line that is concise and works well on mobile devices. Don't hesitate to use emojis to add personality. Similarly, create an informative pre-header to provide extra context.

2. **Layout**: For a simple and mobile-friendly design, consider a single-column layout. This layout often works best for email content.

3. **Width**: A width of 600 pixels is a standard for email layouts, helping ensure compatibility across different email clients.

4. **Web Fonts**: Utilize web fonts to maintain consistent typography across various email clients and browsers.

5. **Hero Image**: Start your email with a hero image of your company or organization. Include a clear call to action, ensuring that it's visible "above the fold."

6. **HTML Tags**: Use proper HTML tags such as `<h1>`, `<h2>`, and `<p>` to structure your content for readability and SEO.

7. **Alt Text**: Provide meaningful alt descriptions for images to cater to users who rely on audio assistance or have disabilities.

8. **Night Mode Compatibility**: If you use night mode or dark mode colors, ensure they render correctly for users with disabilities and those who prefer dark themes.

9. **Accent Colors**: Choose distinct accent colors for your call-to-action buttons and links to make them stand out.

10. **Footer**: Include an unsubscribe button in the footer, following GDPR guidelines and email marketing regulations.

11. **Web Version Link**: It's a good practice to provide a link to a web version of your email, allowing recipients to view the content in their web browser.

These considerations will help you create well-structured and effective HTML emails that are both visually appealing and accessible to a broad audience.


```html
<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <table>
      <tr>
        <td>Content goes here</td>
      </tr>
    </table>
  </body>
</html>
