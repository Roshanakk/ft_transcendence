import AbstractModalView from "./AbstractModalView.js";

export default class extends AbstractModalView {
  constructor(modal) {
    super(modal);
    this.setTitle("User Change Password Form");
  }

  createDomElements() {
    // Create the container
    const container = document.createElement('div');

    // Create the title
    const title = document.createElement('h2');
    title.textContent = 'Change User Password';
    title.classList.add('modal-title');
    container.appendChild(title);

    // Create the form
    const form = document.createElement('form');
    form.id = 'changePassForm';
    form.onsubmit = (event) => event.preventDefault();
    // form.method = 'POST';

    // Create the CSRF token input (assuming you have a way to get the CSRF token)
    // const csrfTokenInput = document.createElement('input');
    // csrfTokenInput.type = 'hidden';
    // csrfTokenInput.name = 'csrfmiddlewaretoken';
    // csrfTokenInput.value = '{{ csrf_token }}'; // Replace with actual CSRF token value
    // form.appendChild(csrfTokenInput);

    // Create the heading
    // const heading = document.createElement('h1');
    // heading.textContent = 'Change password';
    // form.appendChild(heading);

    // Create the old password input
    const oldPasswordInput = document.createElement('input');
    oldPasswordInput.name = 'old_password';
    oldPasswordInput.placeholder = 'Old password';
    oldPasswordInput.type = 'password';
    oldPasswordInput.required = true;
    form.appendChild(oldPasswordInput);
      form.appendChild(document.createElement('br'));

    // Create the new password input
    const newPassword1Input = document.createElement('input');
    newPassword1Input.name = 'new_password1';
    newPassword1Input.placeholder = 'New password';
    newPassword1Input.type = 'password';
    newPassword1Input.required = true;
    form.appendChild(newPassword1Input);
    form.appendChild(document.createElement('br'));

    // Create the confirm password input
    const newPassword2Input = document.createElement('input');
    newPassword2Input.name = 'new_password2';
    newPassword2Input.placeholder = 'Confirm password';
    newPassword2Input.type = 'password';
    newPassword2Input.required = true;
    form.appendChild(newPassword2Input);

    // Create the message paragraph
    const messageParagraph = document.createElement('p');
    const messageSpan = document.createElement('span');
    messageSpan.id = 'message';
    messageSpan.classList.add('message');
    messageParagraph.appendChild(messageSpan);
    form.appendChild(messageParagraph);

    // Create the submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Update';
    form.appendChild(submitButton);

    // Append the form to the container
    container.appendChild(form);

    // Assuming you want to append this container to the body or another element
    return container;
  }

  async afterRender() {
    document.getElementById('changePassForm').addEventListener('submit', async(event) => {
      // Create form 
      const form = event.target;
      const formData = new FormData(form);

      const content = {
        method: 'POST',
        headers: {
          // 'accept': 'application/json',
          // 'content-type': 'application/json',
          'x-csrftoken': this.getCookie('csrftoken')
        },
        // body: json.stringify(data)
        body: formData
      };

      console.log(content);

      try {
        const response = await fetch(`/password_change/`, content);
        const result = await response.json();
        const messageDiv = document.getElementById('message');

        if (response.ok) {
          messageDiv.style.color = 'var(--success-color)';
          messageDiv.textContent = result.message;
          navigateTo(result.redirect);
        } else {
          messageDiv.textContent = '';

          for (const [key, value] of Object.entries(result.errors)) {
            const errorMessage = document.createElement('p');
            errorMessage.classList.add('message');
            errorMessage.textContent = `${key}: ${value}`;
            messageDiv.appendChild(errorMessage);
          }
        }
      } catch (error) {
        console.error('Error:', error);
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = 'An error occurred. Please try again.';
      }
    });
  }
}