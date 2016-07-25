var gulp = require('gulp');
var sass = require('gulp-sass');
var runSequence = require('run-sequence');

gulp.task('sass', function(){
  return gulp.src('codango/static/scss/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('codango/static/css'));
});

gulp.task('watch', function(){
  gulp.watch('codango/static/scss/*.scss', ['sass']);
})

gulp.task('default', function (callback) {
  runSequence(['sass', 'watch'],
    callback
  )
})