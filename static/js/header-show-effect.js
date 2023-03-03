anime({
	targets: ".anim",
	opacity: [0, 1],
	easing: "easeInOutSine",
	duration: 500,
	delay: function (el, i) {
		return i * 100;
	},
	direction: "normal",
	loop: false,
});