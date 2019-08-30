import argparse
import os
from lib.exporter.timeslice import TimeSliceExporter

# python export_run.py run0406_ID000126.fits --template-model run0406_ID000126.xml --tmax 1800
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an obeservations list from a spectra fits")
    parser.add_argument("input_fits",     help="the fits file with times/energies/spectra data")
    parser.add_argument("template_model", help="the xml template")
    parser.add_argument("--tmax",      help="the final observations time in seconds", type=int)
    parser.add_argument("-d", "--dir", help="the savings directory (default: data/)", default="data")
    parser.add_argument("--save",      help="save the time slices metadata in file")
    parser.add_argument("--force",     help="force the overwriting", default=False, action="store_true")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()

    # export the model for each time slice
    exporter = TimeSliceExporter(args.input_fits, template_model=args.template_model, savings_dir=args.dir, verbosity=args.verbose, tmax=args.tmax)
    time_slices = exporter.export(force=args.force)
    if args.save:
        exporter.save(args.save, time_slices, headers=['id', 'tsec', 'model_file', 'ene_flux_file'], delimiter="\t")
    elif args.verbose:
        print(time_slices)
    exit(0)
