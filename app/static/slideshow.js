var slides = document.querySelectorAll('#slides .slide');
var currentSlide = Math.floor(Math.random() * (slides.length));

for (var i=0; i<slides.length; i++) {
	slides[i].style.display='static';
}

slides[currentSlide].className = 'slide showing';


var slideInterval = setInterval(nextSlide, 5000);

function nextSlide() {
	slides[currentSlide].className = 'slide';
	currentSlide = (currentSlide+1)%slides.length;
	slides[currentSlide].className = 'slide showing';
}