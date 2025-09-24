import numpy as np
from matplotlib import pyplot as plt
import sys
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

def python_example(samples=10000):
    # Histogram filled with a normal distribution
    # Create a random number generator with a fixed seed for reproducibility
    rng = np.random.default_rng(19680801)

    n_bins = 50
    mean=100
    sigma=6

    # Generate a normal distribution
    dist = rng.standard_normal(samples)*sigma+mean

    # Set the number of bins with the *bins* keyword argument.
    bins=plt.hist(dist, bins=n_bins)
    yb=bins[0]  # bin contents
    xb=bins[1]  # bin edges
    err=np.sqrt(yb)
    #Calculate bin centers (you can probably find a smarter way to do this!)
    bc=(xb[1:]-xb[:-1])/2+xb[:-1]

    # plot
    fig1, axs1 = plt.subplots(1,1)
    axs1.set_title('random gauss')
    axs1.set_xlabel('x')
    axs1.set_ylabel('frequency')
    axs1.set_xlim(50,150)
    axs1.set_ylim(0, 725)
    axs1.errorbar(bc, yb, yerr=err, fmt=".", color="b")
    axs1.grid()
    # add minor ticks in increments of 2 on x and 25 on y axis
    axs1.xaxis.set_minor_locator(MultipleLocator(2))
    axs1.yaxis.set_minor_locator(MultipleLocator(25))
    plt.savefig("canvas1_py.png")

    # # A multi panel plot
    fig2, axs2 = plt.subplots(2,2)
    fig2.set_size_inches(12, 6)
    axs2[0,0].errorbar(bc, yb, yerr=err, fmt=".", color="b")
    axs2[0,0].set_title('random gauss')
    axs2[0,0].set_xlabel('x')
    axs2[0,0].set_ylabel('frequency')
    axs2[0,0].set_xlim(50,150)
    axs2[0,0].set_ylim(0, 725)
    axs2[0,0].grid()
    # add minor ticks in increments of 2 on x and 25 on y axis
    axs2[0,0].xaxis.set_minor_locator(MultipleLocator(2))
    axs2[0,0].yaxis.set_minor_locator(MultipleLocator(25))
    

    # # add a random uniform offset to the histogram
    offset1 = np.random.uniform(50,150,samples//3)
    dist1 = np.append(dist,offset1)

    bins1=plt.hist(dist1, bins=n_bins)
    yb1=bins1[0]  # bin contents
    xb1=bins1[1]  # bin edges
    err1=np.sqrt(yb1)
    #Calculate bin centers (you can probably find a smarter way to do this!)
    bc1=(xb1[1:]-xb1[:-1])/2+xb1[:-1]

    axs2[0,1].errorbar(bc1, yb1, yerr=err1, fmt=".", color="b")
    axs2[0,1].set_title('Gauss + offset')
    axs2[0,1].set_xlabel('x')
    axs2[0,1].set_ylabel('frequency')
    axs2[0,1].set_xlim(50,150)
    # axs2[0,1].set_ylim(0, 750)
    axs2[0,1].grid()
    # add minor ticks in increments of 2 on x and 25 on y axis
    axs2[0,1].xaxis.set_minor_locator(MultipleLocator(2))
    axs2[0,1].yaxis.set_minor_locator(MultipleLocator(25))


    # apply an offset to give us a 1/x^2 baseline
    # want to generate numbers between 1 and 10 according to a 1/x^2 distribution
    possibilities = np.linspace(1,10,10000)
    weights = np.power(possibilities, -2)
    offset2 = np.random.choice(possibilities, samples*30, p=weights/np.sum(weights))*10 + 40
    dist2 = np.append(dist, offset2)

    bins2 = plt.hist(dist2, bins=n_bins)
    yb2=bins2[0]  # bin contents
    xb2=bins2[1]  # bin edges
    err2=np.sqrt(yb2)
    #Calculate bin centers (you can probably find a smarter way to do this!)
    bc2=(xb2[1:]-xb2[:-1])/2+xb2[:-1]

    axs2[1,0].errorbar(bc2, yb2, yerr=err2, fmt=".", color="b")
    axs2[1,0].set_title('Gauss + offset2')
    axs2[1,0].set_xlabel('x')
    axs2[1,0].set_ylabel('frequency')
    axs2[1,0].set_xlim(50,150)
    # axs2[1,0].set_ylim(0, 750)
    axs2[1,0].grid()
    axs2[1,0].set_yscale("log")
    # add minor ticks in increments of 2 on x and 25 on y axis
    axs2[1,0].xaxis.set_minor_locator(MultipleLocator(2))
    # axs2[1,0].yaxis.set_minor_locator(MultipleLocator(25))


    # do a double gaussian
    gauss2 = rng.standard_normal(samples//2)*20+100
    dist3 = np.append(dist, gauss2)

    bins3 = plt.hist(dist3, bins=n_bins)
    yb3=bins3[0]  # bin contents
    xb3=bins3[1]  # bin edges
    err3=np.sqrt(yb3)
    #Calculate bin centers (you can probably find a smarter way to do this!)
    bc3=(xb3[1:]-xb3[:-1])/2+xb3[:-1]
    axs2[1,1].clear()
    axs2[1,1].errorbar(bc3, yb3, yerr=err3, fmt=".", color="b")
    axs2[1,1].set_title('Double Gaussian')
    axs2[1,1].set_xlabel('x')
    axs2[1,1].set_ylabel('frequency')
    axs2[1,1].set_xlim(50,150)
    # axs2[1,0].set_ylim(0, 750)
    axs2[1,1].grid()
    # axs2[1,1].set_yscale("log")
    # add minor ticks in increments of 2 on x and 25 on y axis
    axs2[1,1].xaxis.set_minor_locator(MultipleLocator(2))
    axs2[1,1].yaxis.set_minor_locator(MultipleLocator(250))


    # hist2 = hist1.Clone("hist2")
    # hist2.SetTitle("Gauss+offset;x;frequency")
    # for i in range(samples//3):
    #     hist2.Fill(tr.Uniform(50,150))
    # tc2.cd(2)
    # hist2.Draw("e")

    # # apply an offset to give us a 1/x^2 baseline
    # hist3 = hist1.Clone("hist3")
    # hist3.SetTitle("Gauss+offset2;x;frequency")
    # base2 = r.TF1("base2","1/x/x",1,10)
    # for i in range(samples*30):
    #     x = base2.GetRandom()*10+40;
    #     hist3.Fill(x)
    # tc2.cd(3).SetLogy()
    # hist3.Draw("e")

    # # a double gaussian
    # hist4 = hist1.Clone("hist4")
    # hist4.SetTitle("Double Gaussian;x;frequency")
    # fpeak.SetParameter(1,20)
    # hist4.FillRandom("fpeak",samples//2)
    # tc2.cd(4)
    # hist4.Draw("e")

    # tc2.Update()
    # input("hit 'return' to continue")

    # # save our plot outputs
    # tc1.SaveAs("canvas1.png")
    # tc2.SaveAs("canvas2.pdf")

    plt.tight_layout()
    plt.savefig("canvas2_py.pdf")
    
if __name__ == '__main__':
    samples=10000
    if len(sys.argv)>1: samples=int(sys.argv[1])
    python_example(samples)
