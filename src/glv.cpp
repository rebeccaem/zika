/*-------------------------------------------------------------------
 *
 * Copyright (C) 2012 The PECOS Development Team
 *
 * Please see http://pecos.ices.utexas.edu for more information.
 *
 * This file is part of the QUESO Library (Quantification of Uncertainty
 * for Estimation, Simulation and Optimization).
 *
 * QUESO is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * QUESO is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with QUESO. If not, see <http://www.gnu.org/licenses/>.
 *
 *-------------------------------------------------------------------
 */
 /*------------------------------------------------------------------
 * Brief description of this file: 
 * 
 * This is the inverse problem to calibrate the 5 rate constants for the 5
 * reaction reduced model of hydrogen combustion.
 *
 * Right now we don't have a set QoI, but there will probably be one in the near
 * future.
 * 
 * The code consists of 7 files:
 * - 'hydrogen_5.C' (this file)
 * - 'compute.C' (the driving application code)
 * - 'compute.h'
 * - 'likelihood.C' (necessary for the SIP)
 * - 'likelihood.h'
 * - 'qoi.C' (necessary for the SFP)
 * - 'qoi.h'
 *-----------------------------------------------------------------*/

#include <compute.h>

int main(int argc, char* argv[])
{
  // Initialize QUESO environment
  MPI_Init(&argc,&argv);
  QUESO::FullEnvironment* env =
    new QUESO::FullEnvironment(MPI_COMM_WORLD,argv[1],"",NULL);

  // Call application
  computeParams(*env);

  // Finalize QUESO environment
  delete env;
  MPI_Finalize();

  return 0;
}
