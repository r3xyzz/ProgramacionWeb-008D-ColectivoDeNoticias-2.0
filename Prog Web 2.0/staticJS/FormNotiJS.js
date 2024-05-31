document.getElementById('imagen').addEventListener('change', function(event) {
    var imagePreview = document.getElementById('image-preview');
    imagePreview.src = URL.createObjectURL(event.target.files[0]);
  });