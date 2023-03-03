anime({
	targets: ".companytext .el",
	strokeDashoffset: [anime.setDashoffset, 0],
	easing: "easeInOutSine",
	duration: 1500,
	delay: function (el, i) {
		return i * 250 + 500;
	},
	direction: "normal",
	loop: false,
});

anime({
	targets: ".companytext .fill",
	fill: ["#00000000", "#ffc800"],
	easing: "easeInOutSine",
	duration: 1500,
	delay: function (el, i) {
		return i * 250 + 1000;
	},
	direction: "alternate",
	loop: false,
});