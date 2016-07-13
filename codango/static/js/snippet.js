/* global Firebase: true, $:true, FB:true, prettyPrint: true, ace:true */
/* eslint no-var: 0, func-names: 0*/
/* eslint no-alert: 0, func-names: 0*/
$(document).ready(function () {
  var snippet = $('#snippet');
  var editor = ace.edit('editor');
  editor.setTheme('ace/theme/twilight');
  editor.session.setMode('ace/mode/python');
  snippet_text = $('#snippet').attr('data');
  if (snippet_text){
    editor.getSession().setValue(snippet_text)
  }
  editor.getSession().on('change', function () {
    snippet.val(editor.getSession().getValue());
  });
});
