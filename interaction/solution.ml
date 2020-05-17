let () =
  let ic = open_in "flag" in
  let line = input_line ic in
  print_endline line;
  flush stdout;
  close_in ic
