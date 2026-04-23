echo "Results for every graph\n" > "$1"
echo "" > "$1"

for g in graph*.json; do
  echo "$g" >> "$1"
  echo "" >> "$1"
  echo "$g"
  perf stat -- ./build/problem_program_b "$g" | tee -a "$1" 
done
