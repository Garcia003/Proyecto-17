module.exports = {
	globDirectory: '.',
	globPatterns: [
		'**/*.{css,jpg,png,js,txt,json,scss,woff,woff2,eot,svg,ttf,cjs,php,html}'
	],
	swDest: 'sw.js',
	ignoreURLParametersMatching: [
		/^utm_/,
		/^fbclid$/
	]
};