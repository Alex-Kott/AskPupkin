$("#tag-cloud span").each(function(i, tag){
	var style = {
		'font-size': rand(0.8, 2)+'em',
		'color'	: randColor()
	}
	$(tag).css(style)
})

function rand(min, max)
{
  return Math.random() * (max - min) + min;
}

function randColor() {
	var letters = '0123456789ABCDEF';
	var color = '#';
	for (var i = 0; i < 6; i++) {
		color += letters[Math.floor(Math.random() * 16)];
	}
	return color;
}



// tags
// https://stackoverflow.com/filter/tags?q=javas&newstyle=true
