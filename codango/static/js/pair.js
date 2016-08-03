/* global Firebase: true, $:true, FB:true, prettyPrint: true,
  ace:true, Firepad: true, FirepadUserList: true*/
/* eslint no-var: 0, func-names: 0*/
/* eslint no-alert: 0, func-names: 0*/
var FIRBASE_URL = Config.firebaseUrl;
var session = null;
var editor = null;
var userid = Cookies.get('userid');
var displayName = $('#username').attr('value');
var firepadRef = new Firebase(FIRBASE_URL);
var sessionId = $('#session-id').val();

/**
 * Handles ace editor initialization
 * @param {string} langauge - the programming language of the session
 * @param {object} theme - the present theme being used by the session
 */
function changeEditorOption(language, theme) {
  editor.setTheme('ace/theme/' + theme);
  session.setMode('ace/mode/' + language);
}

$(document).ready(function () {
  var app = {
    init: function (selectedLanguage, selectedTheme) {
      // Set defaults for the theme and language

      save_theme = localStorage.getItem('theme')
      if(save_theme){
        $('#theme').val(save_theme);
      }
      var theme = selectedTheme || save_theme || 'cobalt';
      var language = selectedLanguage || 'python';

      // Get current session firebase ref
      editor = ace.edit('firepad-container');
      session = editor.getSession();
      app.bindEvents();
      // Initialize ACE Editor
      editor.setTheme('ace/theme/' + theme);
      session.setUseWrapMode(true);
      session.setUseWorker(false);
      session.setMode('ace/mode/' + language);
      pageRef = app.getPageRef();
      var firePad = Firepad.fromACE(pageRef, editor);
      var firepadUserList = FirepadUserList.fromDiv(pageRef.child('users/'+
         sessionId), document.getElementById('userlist'), userid, displayName);
    },
    bindEvents: function () {
      // Language change event handler
      $('#language').change(function () {
        var lang = $(this).val();
        var theme = $('#theme').val();
        changeEditorOption(lang, theme);
        app.updateSession(lang);
      });

      // Theme change event handler
      $('#theme').change(function () {
        var theme = $(this).val();
        var lang = $('#language').val();
        changeEditorOption(lang, theme);

        localStorage.setItem('theme', theme)
      });
    },
    getPageRef: function () {
      return firepadRef.child('session/' + sessionId);
    },
    updateSession: function (lang) {
      // Update the programming language of session
      var sessionId = $('#session-id').val();
      $.ajax({
        url: '/pair/'+sessionId,
        type: 'PUT',
        data: {
          'language': lang
        }
      });
    }
  };
 app.init();
});
