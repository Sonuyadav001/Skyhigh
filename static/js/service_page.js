document.addEventListener("DOMContentLoaded", function () {
  const modalElement = document.getElementById("productModal");
  const triggerButton = document.querySelector('[data-bs-toggle="modal"]');

  // Show the modal and handle accessibility
  modalElement.addEventListener("show.bs.modal", function () {
    modalElement.removeAttribute("inert");
    modalElement.setAttribute("aria-hidden", "false");

    // Move focus to the modal title for accessibility
    const modalTitle = modalElement.querySelector(".modal-title");
    if (modalTitle) modalTitle.focus();
  });

  // Hide the modal and restore accessibility settings
  modalElement.addEventListener("hide.bs.modal", function () {
    modalElement.setAttribute("aria-hidden", "true");
    modalElement.setAttribute("inert", "");

    // Return focus to the trigger button
    if (triggerButton) triggerButton.focus();
  });
});

/**
 * Function to show product details in a modal.
 * @param {string} title - The title of the product.
 * @param {Array<string>} details - An array of details about the product.
 * @param {string} image - The full URL of the product image.
 */
function showDetails(title, details, image) {
  const modalTitleElement = document.getElementById("productModalLabel");
  const modalImageElement = document.getElementById("modalImage");
  const modalListElement = document.getElementById("modalList");

  // Update modal title
  if (modalTitleElement) {
    modalTitleElement.textContent = title;
  }

  // Update modal image
  if (modalImageElement) {
    modalImageElement.src = image;
    modalImageElement.alt = title; // Accessibility: meaningful alt text
  }

  // Update modal details list
  if (modalListElement) {
    modalListElement.innerHTML = ""; // Clear existing list items
    details.forEach((detail) => {
      const listItem = document.createElement("li");
      listItem.textContent = detail;
      modalListElement.appendChild(listItem);
    });
  }

  // Show the modal using Bootstrap's API
  const modal = new bootstrap.Modal(document.getElementById("productModal"));
  modal.show();
}
