// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementById('closeBtn');
const form = document.getElementById('multiStepForm');
const steps = Array.from(document.getElementsByClassName('step'));
const prevBtns = Array.from(document.querySelectorAll('button.prev'));
const nextBtns = Array.from(document.querySelectorAll('button.next'));

let currentStep = 0;

function showStep(stepIndex) {
    steps[currentStep].classList.remove('active');
    steps[stepIndex].classList.add('active');
    prevBtns[currentStep].classList.remove('active');
    nextBtns[currentStep].classList.remove('active');
    prevBtns[stepIndex].classList.add('active');
    nextBtns[stepIndex].classList.add('active');
    currentStep = stepIndex;
}

openModalBtn.addEventListener('click', () => {
    modal.style.display = 'block';
    showStep(0);
});

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (currentStep === 3) {
        alert('Form submitted. Check availability here.');
        modal.style.display = 'none';
    }
});

prevBtns.forEach((btn, index) => {
    btn.addEventListener('click', () => showStep(index - 1));
});

nextBtns.forEach((btn, index) => {
    btn.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent form submission
        showStep(index + 1);
    });
});


    // Function to update specialist field based on user input
    function updateSpecialistField() {
        // Get the user input from the patient_condition field
        var patientCondition = document.getElementById('patient_condition').value;

        // Make an AJAX request to the server to get the suggested specialist
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/get_suggested_specialist', true);
        xhr.setRequestHeader('Content-Type', 'application/json');

        // Define the data to be sent to the server (in this case, the patient condition)
        var data = JSON.stringify({ 'patient_condition': patientCondition });

        // Set up the callback function to handle the server's response
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Update the specialist field with the suggested specialist
                document.getElementById('specialist').value = xhr.responseText;
            }
        };

        // Send the AJAX request with the data
        xhr.send(data);
    }

    // Attach the updateSpecialistField function to the input event of the patient_condition field
    document.getElementById('patient_condition').addEventListener('input', updateSpecialistField);

  document.getElementById('patient_condition').addEventListener('input', function() {
        // Call a function to update the specialist suggestion
        updateSpecialistSuggestion();
    });
