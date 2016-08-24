var gulp = require('gulp');
var sass = require('gulp-sass');
var runSequence = require('run-sequence');
var browserify = require('browserify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');

gulp.task('buildreact', function() {
  return browserify({
      entries: 'codango/static/js/components/app.jsx',
      extensions: ['.jsx'],
      debug: true
    })
    .transform('babelify', {
      presets: ['es2015', 'react']
    })
    .bundle()
    .pipe(source('bundle.js'))
    .pipe(gulp.dest('codango/static/js/build'));
});

gulp.task('sass', function() {
  return gulp.src('codango/static/scss/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('codango/static/css'));
});

gulp.task('watch', function() {
  gulp.watch('codango/static/scss/*.scss', ['sass']);
  gulp.watch('codango/static/js/components/*.jsx', ['buildreact']);
});

gulp.task('default', function(callback) {
  runSequence(['sass', 'buildreact', 'watch'],
    callback
  );
});
