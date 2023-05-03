#!/usr/bin/env ruby
# This regular expression must match a 10 digit phone number
puts ARGV[0].scan(/\d{m}/).join
