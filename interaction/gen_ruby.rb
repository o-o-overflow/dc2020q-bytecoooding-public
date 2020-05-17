
code = RubyVM::InstructionSequence.compile("puts File.open('flag', 'r').read").to_binary

out = File.open('ruby_solution', 'w+')
out.puts code
out.close
