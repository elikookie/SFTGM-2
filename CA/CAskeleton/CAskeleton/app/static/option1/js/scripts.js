/*!
* Start Bootstrap - Heroic Features v5.0.5 (https://startbootstrap.com/template/heroic-features)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-heroic-features/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function toggleChildren() {
  var checkBox = document.getElementById("child");
  var childAge = document.getElementById("child_age");
  if (checkBox.checked) {
    childAge.style.display = "block";
  } else {
    childAge.style.display = "none";
  }
}


const prefectures = document.querySelectorAll('.prefecture');

// Add event listeners to each prefecture
prefectures.forEach(prefecture => {
  prefecture.addEventListener('click', (event) => {
    // Remove the 'selected' class from any previously selected element
    const previouslySelected = document.querySelector('.selected');
    if (previouslySelected) {
      previouslySelected.classList.remove('selected');
    }

    // Add the 'selected' class to the clicked element
    event.currentTarget.classList.add('selected');

    // Store the selected value, e.g., in a hidden input field
    const selectedValue = event.currentTarget.id;
    // Do something with the selected value, e.g., update a form field
    console.log('Selected prefecture:', selectedValue);
  });
});

function showTooltip(event) {
  const tooltip = document.getElementById("map-tooltip");
  const prefecture = event.target.getAttribute("data-prefecture");
  tooltip.style.opacity = 1; // Use opacity instead of visibility
  tooltip.textContent = prefecture;
}

function moveTooltip(event) {
  const tooltip = document.getElementById("map-tooltip");
  tooltip.style.left = event.pageX + 20 + "px";
  tooltip.style.top = event.pageY + 20 + "px";
}

function hideTooltip() {
  const tooltip = document.getElementById("map-tooltip");
  tooltip.style.opacity = 0; // Use opacity instead of visibility
}

function selectPrefecture(event) {
    const selectedPrefecture = event.target.getAttribute('data-prefecture');
    const prefectureSelect = document.getElementById('prefecture');

    for (let i = 0; i < prefectureSelect.options.length; i++) {
        if (prefectureSelect.options[i].value === selectedPrefecture) {
            prefectureSelect.selectedIndex = i;
            break;
        }
    }
}
