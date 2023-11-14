// modal uplod button
function uploadPhoto() {
    var input = document.getElementById('photoInput');
    var file = input.files[0];
  
    if (file) {
      if (file.type === 'image/jpeg' || file.type === 'image/png' || file.type === 'image/jpg') {
        // Upload the file
      } else {
        alert('Only JPG, JPEG, and PNG files are allowed.');
      }
    } else {
      alert('No file selected.');
    }
  }
  
  