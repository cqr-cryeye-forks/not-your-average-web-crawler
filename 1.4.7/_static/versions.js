$(document).ready(function() {
	$.getJSON('/not-your-average-web-crawler/releases.json?cache=' + new Date().getTime(), function(releases) {
		var html = "";
		var current = $('#releases').attr('data-selected');

		var index = 1;
		var length = Object.keys(releases).length;

		for (release in releases) {
			var last = index === length;
			var disabled = releases[release] ? '' : 'disabled';
			var selected = current == release ? 'selected' : '';
			var status = !releases[release] ? 'n/a' : last ? 'latest' : 'old';
			var value = !disabled ? '../' + (last ? 'latest' : release) + '/index.html' : '';

			html += '<option ' + disabled + ' ' + selected + ' value="' + value + '">Version ' + release + ' (' + status + ')</option>';

			if (last && current != release) {
				$('#releases').addClass('old');
			}

			index ++;
		}

		$('#releases').html(html);
		$('#releases').removeAttr('disabled');
	});
});