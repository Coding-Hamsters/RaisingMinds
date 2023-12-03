const donateAmountInput = document.querySelector('.donateAmount');
const donateAmountLabel = document.querySelector('.js');
const donateButton = document.getElementById('button-addon2');

donateButton.addEventListener('click', () => {
  const donateAmountValue = parseInt(donateAmountInput.value);
  donateAmountLabel.textContent = `Donate amount : $ ${donateAmountValue}.00`;
});

// Check if there's a stored donate amount value
