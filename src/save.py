import csv

def write_data(path, data):
  with open(path, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data:
      writer.writerow(row)
  print(f"Wrote {len(data)} rows to {path}")