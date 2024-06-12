'use strict';

var path = require('path');
var gulp = require('gulp');
var conf = require('./conf');
var babel = require('gulp-babel');
const concat = require('gulp-concat');

var browserSync = require('browser-sync');

var $ = require('gulp-load-plugins')();


gulp.task('scripts-reload', function() {
  return buildScripts()
    .pipe(browserSync.stream());
});

gulp.task('scripts', function() {
  return buildScripts();
});

function buildScripts() {
  return gulp.src(path.join(conf.paths.src, '/app/**/*.js'))
    .pipe($.eslint({ "env": { "es6": true } }))
    .pipe($.eslint.format())
    .pipe($.size())
};
